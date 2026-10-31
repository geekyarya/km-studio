"""Generates Kiara's image (Flux + her LoRA) and animates it to video via fal.ai."""
import os

import fal_client

import persona

IMAGE_MODEL = os.getenv("FAL_IMAGE_MODEL", "fal-ai/flux-lora")
VIDEO_MODEL = os.getenv("FAL_VIDEO_MODEL", "fal-ai/kling-video/v2.1/standard/image-to-video")
LORA_URL = os.getenv("KIARA_LORA_URL")  # URL of Kiara's trained face LoRA (.safetensors)


def make_image(plan: dict) -> str:
    prompt = f"{persona.LOOK}, wearing {plan['outfit']}, at {plan['location']}, {plan['pose_expression']}"
    args = {"prompt": prompt, "image_size": "portrait_16_9", "num_images": 1}
    if LORA_URL:
        args["loras"] = [{"path": LORA_URL, "scale": 1.0}]
    result = fal_client.subscribe(IMAGE_MODEL, arguments=args)
    return result["images"][0]["url"]


def make_video(plan: dict, image_url: str) -> str:
    result = fal_client.subscribe(
        VIDEO_MODEL,
        arguments={
            "image_url": image_url,
            "prompt": f"{plan['video_motion']}, natural realistic movement, cinematic",
            "duration": "5",
        },
    )
    return result["video"]["url"]
