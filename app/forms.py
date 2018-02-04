from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Sign In')
	
class OptionsForm(FlaskForm):
	watching = BooleanField('Watching')
	completed = BooleanField('Completed', default='checked')
	onhold = BooleanField('On-Hold')
	dropped = BooleanField('Dropped')
	plantowatch = BooleanField('Plan to Watch')
	
	tv = BooleanField('TV', default='checked')
	movie = BooleanField('Movie')
	special = BooleanField('Special')
	ova = BooleanField('OVA')
	ona = BooleanField('ONA')
	
	submit = SubmitField('GO')
	
	def validate(self):
		if not super().validate():
			return False
		stSelected = False
		tpSelected = False
		for st in [self.watching, self.completed, self.onhold, self.dropped, self.plantowatch]:
			if st.data:
				stSelected = True
				break
		for tp in [self.tv, self.movie, self.special, self.ova, self.ona]:
			if tp.data:
				tpSelected = True
				break
		if stSelected and tpSelected:
			return True
		else:
			self.submit.errors.append('You must select at least one status and one type!')
			return False