from dashscope import TextToImage

class FabGenieAgent:
    def generate_image(self, prompt):
        response = TextToImage.call(
            prompt=prompt,
            model="wanx-v1",
            size="1024*1024"
        )
        return response.output.url

    def run(self, user_input):
        image_url = self.generate_image(f"工业设计高清渲染图，{user_input}，白底，4K")
        return f"生成的概念图地址：{image_url}"
