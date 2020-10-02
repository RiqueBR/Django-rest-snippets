from django.db import models
from pygments.lexers import get_all_lexers
from pygments.lexers import get_lexer_by_name

from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here
class Snippet(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	code = models.TextField()
	linenos = models.BooleanField(default=False)
	language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
	style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
	owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
	highlighted = models.TextField()


	# override the default 'save' method of this class
	def save(self, *args, **kwargs):
		'''
		Use pygments library to make a pretty html version of the snippet
		'''
		lexer = get_lexer_by_name(self.language)
		linenos = 'table' if self.linenos else False
		options = {'title':self.title} if self.title else {}
		formatter = HtmlFormatter()
		self.highlighted = highlight(self.code, lexer, formatter)
		super(Snippet, self).save(*args, **kwargs)

	class Meta:
		ordering = ['created']