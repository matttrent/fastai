import os
import pathlib
from gans.options.feedback_options import FeedbackOptions
from gans.data import CreateDataLoader
from gans.models import create_model
from gans.util.visualizer import Visualizer
from gans.util import html
from gans.util.util import save_image

opt = FeedbackOptions().parse()
opt.phase = 'feedback'
opt.nThreads = 1   # test code only supports nThreads = 1
opt.batchSize = 1  # test code only supports batchSize = 1
opt.serial_batches = True  # no shuffle
opt.no_flip = True  # no flip

data_loader = CreateDataLoader(opt)
dataset = data_loader.load_data()
model = create_model(opt)
visualizer = Visualizer(opt)


for i, data in enumerate(dataset.dataset):
    if i >= opt.how_many:
        break
    data['A'] = data['A'].unsqueeze(0)
    data['B'] = data['B'].unsqueeze(0)
    model.set_input(data)
    model.test()
    visuals = model.get_current_visuals()

    save_path = dataset.dataset.path_for_index(i + 1)
    save_image(visuals['fake_B'], save_path)
