import comfy_extras.nodes_upscale_model

class ImageUpscaleWithModelMultipleTimes:
	@classmethod
	def INPUT_TYPES(s):
		return {
			"required": {
				"upscale_model": ("UPSCALE_MODEL", ),
				"image": ("IMAGE", ),
				"times": ("INT", {"default": 1, "min": 1}),
			}
		}
	RETURN_TYPES = ("IMAGE",)
	FUNCTION = "upscale"

	CATEGORY = "image/upscaling"

	def upscale(self, upscale_model, image, times):
		for _ in range(times):
			image = comfy_extras.nodes_upscale_model.ImageUpscaleWithModel.upscale(self, upscale_model, image)[0]
		return (image, )
