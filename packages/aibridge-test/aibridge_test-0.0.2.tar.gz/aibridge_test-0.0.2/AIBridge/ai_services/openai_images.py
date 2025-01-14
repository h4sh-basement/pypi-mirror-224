from AIBridge.prompts.prompt_completion import Completion
from AIBridge.ai_services.ai_abstraction import AIInterface
from AIBridge.exceptions import OpenAIException, AIBridgeException
import json
import uuid
from AIBridge.constant.constant import OPENAI_IMAGE_TYPE, OPENAI_IMAGE_SIZES
import openai
from AIBridge.constant.common import parse_api_key
from AIBridge.ai_services.image_optimisaton import ImageOptimise


class OpenAIImage(AIInterface):
    @classmethod
    def generate(
        self,
        prompts: list[str] = [],
        prompt_ids: list[str] = [],
        prompt_data: list[dict] = [],
        variables: list[dict] = [],
        image_data: list[str] = [],
        mask_image: list[str] = [],
        variation_count: int = 1,
        size: str = "1024x1024",
        process_type: str = "create",
        message_queue=False,
    ):
        try:
            if prompts and prompt_ids:
                raise OpenAIException(
                    "please provide either prompts or prompts ids at atime"
                )
            if not prompts and not prompt_ids:
                raise OpenAIException(
                    "Either provide prompts or prompts ids to genrate the data"
                )
            if process_type not in OPENAI_IMAGE_TYPE:
                raise OpenAIException(
                    "process_type can be either create, variation, edit"
                )
            if size not in OPENAI_IMAGE_SIZES:
                raise OpenAIException(
                    "size can be either 1024x1024 or 512x512 or 256x256"
                )
            if process_type == "edit" or process_type == "variation":
                if not image_data:
                    raise OpenAIException("Please enter image for edit or variation")
            if mask_image:
                if len(mask_image) != len(image_data):
                    raise OpenAIException(
                        "mask_image length should be equal to image_data length",
                    )
            if prompt_ids:
                prompts_list = Completion.create_prompt_from_id(
                    prompt_ids=prompt_ids,
                    prompt_data_list=prompt_data,
                    variables_list=variables,
                )
            if prompts:
                if prompt_data or variables:
                    prompts_list = Completion.create_prompt(
                        prompt_list=prompts,
                        prompt_data_list=prompt_data,
                        variables_list=variables,
                    )
                else:
                    prompts_list = prompts
            if image_data:
                if prompts_list:
                    if len(image_data) != len(prompts_list):
                        raise OpenAIException(
                            "image_data length should be equal to prompts length",
                        )
            if message_queue:
                id = uuid.uuid4()
                message_data = {
                    "id": str(id),
                    "prompts": json.dumps(prompts_list),
                    "variation_count": variation_count,
                    "ai_service": "open_ai_image",
                    "image_data": json.dumps(image_data),
                    "mask_image": json.dumps(mask_image),
                    "size": size,
                    "process_type": process_type,
                }
                message = {"data": json.dumps(message_data)}
                from AIBridge.queue_integration.message_queue import MessageQ

                MessageQ.mq_enque(message=message)
                return {"response_id": str(id)}
            return self.get_response(
                prompts=prompts_list,
                image_data=image_data,
                mask_image=mask_image,
                variation_count=variation_count,
                size=size,
                process_type=process_type,
            )
        except AIBridgeException as e:
            raise OpenAIException(f"{e}")

    @classmethod
    def get_response(
        self,
        prompts,
        image_data=[],
        mask_image=[],
        variation_count=1,
        size="1024*1024",
        process_type="create",
    ):
        try:
            OPEN_AI_API_KEY = parse_api_key("open_ai")
            openai.api_key = OPEN_AI_API_KEY
            data = {}
            if image_data:
                image_data = ImageOptimise.get_image(image_data)
                if mask_image:
                    mask_image = ImageOptimise.get_image(mask_image)
                    mask_image = ImageOptimise.set_dimension(image_data, mask_image)
                    mask_image = ImageOptimise.get_bytes_io(mask_image)
                image_data = ImageOptimise.get_bytes_io(image_data)
            if process_type == "create":
                for index, prompt in enumerate(prompts):
                    response = openai.Image.create(
                        prompt=prompt, n=variation_count, size=size
                    )
                    data[str(index)] = [{"url": obj["url"]} for obj in response["data"]]
            elif process_type == "edit":
                for index, prompt in enumerate(prompts):
                    image = image_data[index]
                    mask = None
                    if mask_image:
                        mask = mask_image[index]
                    response = openai.Image.create_edit(
                        image=image,
                        mask=mask,
                        prompt=prompt,
                        n=variation_count,
                        size=size,
                    )
                    data[str(index)] = [{"url": obj["url"]} for obj in response["data"]]
            elif process_type == "variation":
                for index, image in enumerate(image_data):
                    response = openai.Image.create_variation(
                        image=image, n=variation_count, size=size
                    )
                    data[str(index)] = [{"url": obj["url"]} for obj in response["data"]]
            return data
        except AIBridgeException as e:
            raise OpenAIException(f"Error in creating image using open ai{e}")
