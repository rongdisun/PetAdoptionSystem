from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django import forms
from user.models import User, UserProfile

# Register your models here.

admin.site.unregister(Group)


# 创建用户表单，用于在 admin 界面中添加新用户
class UserCreationForm(forms.ModelForm):
    # 定义密码输入字段，使用 PasswordInput 小部件以隐藏输入内容
    password1 = forms.CharField(label="密码", widget=forms.PasswordInput)
    password2 = forms.CharField(label="确认密码", widget=forms.PasswordInput)

    class Meta:
        model = User
        # 指定表单包含的字段，这些字段将在 admin 界面中显示
        fields = ('userid', 'username', 'is_staff', 'is_active')

    def clean_password2(self):
        # 验证两次输入的密码是否一致
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("两次输入的密码不一致")
        return password2

    def save(self, commit=True):
        # 保存用户时对密码进行加密处理
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# 修改用户表单，用于在 admin 界面中编辑已有用户
class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        # 指定编辑时显示的字段
        fields = ('userid', 'username', 'is_staff', 'is_active')


# 为 User 模型配置 admin 界面
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # 指定编辑用户时使用的表单
    form = UserChangeForm
    # 指定添加用户时使用的表单
    add_form = UserCreationForm

    # 配置列表页面显示的字段
    list_display = ('userid', 'username', 'is_staff', 'is_active', 'is_superuser')
    # 配置列表页面的过滤器
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    # 配置编辑页面的字段分组
    fieldsets = (
        (None, {'fields': ('userid', 'username', 'password')}),
        ('权限', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    # 配置添加用户页面的字段分组
    add_fieldsets = (
        (None, {
            'classes': ('wide',),  # 设置表单宽度为宽
            'fields': ('userid', 'username', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    # 配置搜索字段，支持按 userid 和 username 搜索
    search_fields = ('userid', 'username')
    # 配置默认排序字段
    ordering = ('userid',)
    # 配置权限和用户组的多选框为水平布局
    filter_horizontal = ('groups', 'user_permissions',)


# 定义 UserProfile 的内联 admin，嵌入到 User 的 admin 界面中
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False  # 禁止删除内联的 UserProfile
    verbose_name_plural = '用户资料'  # 设置内联显示的名称
    fieldsets = (
        (None, {
            'fields': (
                'avatar',
                'birthdate',
                'sex',
                'address',
                'email',
                'telephone',
                'identity_type',
                'identity_number',
            )
        }),
    )


# 扩展 UserAdmin 以包含 UserProfile 内联
class ExtendedUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


# 为 UserProfile 模型单独注册 admin 界面
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # 配置列表页面显示的字段
    list_display = ('user', 'sex', 'email', 'telephone', 'identity_type')
    # 配置列表页面的过滤器
    list_filter = ('sex', 'identity_type')
    # 配置搜索字段，支持按关联用户的 userid、username 以及其他字段搜索
    search_fields = ('user__userid', 'user__username', 'email', 'telephone', 'identity_number')
    # 配置编辑页面的字段分组
    fieldsets = (
        (None, {
            'fields': (
                'user',
                'avatar',
                'birthdate',
                'sex',
                'address',
                'email',
                'telephone',
                'identity_type',
                'identity_number',
            )
        }),
    )
    # 设置 user 字段为只读，防止在 UserProfile admin 中修改关联用户
    readonly_fields = ('user',)


# 取消默认的 User admin 注册，并注册扩展后的版本
admin.site.unregister(User)
admin.site.register(User, ExtendedUserAdmin)
