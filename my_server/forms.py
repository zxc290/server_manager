from .models import Server
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit


class AddServerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-inline'
        self.helper.form_show_labels = False
        self.helper.form_id = 'add-server-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'add_server'
        self.helper.layout = Layout(
            Field('ip_address', placeholder='服务器地址'),
            Field('game', placeholder='游戏名'),
            Field('area', placeholder='游戏区服'),
            Submit('confirm-add', '新增', css_class='btn btn-primary'),
        )

    class Meta:
        model = Server
        fields = ['ip_address', 'game', 'area']


class EditServerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'edit-server-form'

    class Meta:
        model = Server
        fields = ['ip_address', 'game', 'area']