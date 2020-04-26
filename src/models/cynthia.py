
class patcher(patcher):
    def __init__(self, body='./body/body_cynthia.png', **options):
        super().__init__(name='シンシア', body=body, pantie_position=[0,0], **options)

    def convert(self, image):
        return image
