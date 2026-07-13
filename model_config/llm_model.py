from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from transformers.pipelines import pipeline
from config.logger import get_logger
from config.config import LLM_MODEL_NAME
import torch


logger = get_logger("llm-model")


class LLMModel:
    def __init__(self, model_name=LLM_MODEL_NAME):

        try:
            if not model_name:
                raise ValueError("LLM model name empty or none")

            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            logger.info("Device loaded successfully")

            logger.info("Loading tokenizer...")
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            logger.info("tokenizer loaded")

            logger.info("Loading quantization config...")
            bits_and_bytes_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_use_double_quant=True,
                bnb_4bit_compute_dtype=torch.float16,
            )

            logger.info("Loading model...")
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name, quantization_config=bits_and_bytes_config, device_map="auto"
            )
            logger.info("Model loaded")

            logger.info("Creating pipeline...")
            pipe = pipeline(
                "text-generation",
                model=self.model,
                tokenizer=self.tokenizer,
                max_new_tokens=1000,
                do_sample=False,
                return_full_text=False,
            )

            self.llm = HuggingFacePipeline(pipeline=pipe)
            logger.info("LLM loaded successfully")

        except ValueError as e:
            logger.error(f"Value error: {e}")
            raise

        except Exception as e:
            logger.error(f"Error in llm model initialization: {e}")
            raise
