from django import forms
from .models import Movie

class MovieForm(forms.Form):
    title = forms.CharField(max_length=100)
    title_en = forms.CharField(max_length=100)
    audience = forms.IntegerField()
    open_date = forms.DateField(
                widget=forms.widgets.DateInput(attrs={"type":"date"})
                )
    genre = forms.CharField(max_length=100)
    watch_grade = forms.CharField(max_length=100)
    score = forms.FloatField()
    poster_url = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea())
    
    
class MovieModelForm(forms.ModelForm):
    # Meta클래스 오버라이딩
    class Meta:
        # 기본적으로 두가지 항목을 넣게 되어 있음
        
        # 모델을 알려주면 자동으로 어울리는 걸 매칭해줌
        model = Movie
        # 전체 필드를 가져오기
        fields = '__all__'
        widgets = {
            "open_date":forms.DateInput(attrs={'type':'date'})
        }
        