from SAC.Config import SACConfig
from SAC.Learner import Learner


config = SACConfig('./cfg/SAC.json')
trainer = Learner(config)
trainer.run()