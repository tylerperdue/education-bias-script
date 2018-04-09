from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random


class word_tools_wordcloud:
    def __init__(self):
        self.d = path.dirname(__file__)
        pass

    def make_wordcloud(self, in_dictionary, out_file):
        the_cloud = WordCloud().generate_from_frequencies(in_dictionary)

        import matplotlib.pyplot as plt
        plt.imshow(the_cloud, interpolation='bilinear')
        plt.axis("off")

        the_cloud = WordCloud(relative_scaling=1, width=2048, height=2048, max_words=2048, min_font_size=1,
                              mode='RGB', normalize_plurals=True).generate_from_frequencies(in_dictionary)
        plt.figure()
        plt.imshow(the_cloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()

        the_cloud.to_file(out_file)

        return the_cloud

    def make_wordcloud_img(self, in_dictionary, in_image, out_file):
        # read the mask_color image
        the_mask = Image.open(path.join(self.d, in_image))
        mask_color = np.array(the_mask)

        # create WordCloud Process
        the_cloud = WordCloud().generate_from_frequencies(in_dictionary)

        import matplotlib.pyplot as plt
        plt.imshow(the_cloud, interpolation='bilinear')
        plt.axis("off")

        the_cloud = WordCloud(background_color='white', mask=mask_color, relative_scaling=1, margin=8, width=4096,
                              height=4096, max_words=9999, min_font_size=5, mode='RGB',
                              normalize_plurals=True, color_func=ImageColorGenerator(mask_color)
                              ).generate_from_frequencies(in_dictionary)

        default_colors = the_cloud.to_array()
        plt.title("Custom colors")
        plt.imshow(the_cloud.recolor(random_state=3),
                   interpolation="bilinear")

        the_cloud.to_file(out_file)

        plt.axis("off")
        plt.figure()
        plt.imshow(default_colors, interpolation="bilinear")
        plt.axis("off")
        plt.show()

        return the_cloud
