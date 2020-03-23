from ckeditor.fields import RichTextFormField

class FooForm(forms.ModelForm):
    class Meta:
          model = Foo
          fields = ['content']
          widgets = {
             'content': RichTextFormField(),
          }