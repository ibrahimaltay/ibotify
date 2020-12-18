from wtforms import Form, StringField, PasswordField, validators

class RegistrationForm(Form):
	
	username = StringField('Username', [validators.Length(min=4, max=25)])
	email = StringField('Email', [validators.Length(min=6, max=35)])
	password = StringField('Password', [validators.Length(min=6, max=100), 
										validators.Required()])