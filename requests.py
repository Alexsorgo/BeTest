import bert
from erlastic import Atom

Auth = Atom('Auth')
Feature = Atom('Feature')
reg = Atom('reg')
stri = (Auth, "reg_234BD084-5883-4E89-B86A-97305E903007", "234BD084-5883-4E89-B86A-97305E903007", [], "8613777322455", [], reg, [], [], [], [(Feature, "234BD084-5883-4E89-B86A-97305E903007__152423881122539", "AppVersion", "0.2.92", "AUTH_DATA"), (Feature, "234BD084-5883-4E89-B86A-97305E903007__152423881122904", "OS", "iOS 11.3", "AUTH_DATA"), (Feature, "234BD084-5883-4E89-B86A-97305E903007__152423881123003", "DeviceModel", "simulator/sandbox", "AUTH_DATA")], [], [], [], [])
login = bert.encode(stri)

verify = Atom('verify')
sms_f = (Auth,[],"234BD084-5883-4E89-B86A-97305E903007",[],"8613777322455",[],verify,"903182",[],[],[],[],[],[],[])
sms = bert.encode(sms_f)

Roster = Atom('Roster')
nick = Atom('nick')
username_f = (Roster,456,[],[],[],"SomeNew",[],[],[],[],[],[],[],nick)
username = bert.encode(username_f)
