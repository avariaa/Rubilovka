class Model:
    def __init__(self, models):
        self.models = models

    def get_model(self, model_class):
        return self.models[model_class]