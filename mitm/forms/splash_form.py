from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

class SplashForm(Form):
    
    def reset(self):
        blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
        self.process(blankData)
