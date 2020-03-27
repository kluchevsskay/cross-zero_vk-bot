from PIL import Image

start_image = Image.open('data/start.jpg')
start_image.show()


def drawing_steps(input_image_path,
                  output_image_path,
                  step_path,
                  position):
    main_image = Image.open(input_image_path)
    step = Image.open(step_path)
    width, height = main_image.size

    deleted_background = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    deleted_background.paste(main_image, (0, 0))
    deleted_background.paste(step, position, mask=step)
    deleted_background.show()
    deleted_background.save(output_image_path)


if __name__ == '__main__':
    img = 'lighthouse.jpg'
    drawing_steps(start_image, 'cross.jpg',
                  'data/step.png', position=(0, 0))

step_image = Image.open('data/step.png')
step_image.show()
