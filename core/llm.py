import os
import json
from typing import Dict, Any, List, Optional
from openai import OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

from huggingface_hub import InferenceClient

class LLMService:
    def __init__(self):
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")
        
        # Default to Zephyr 7B Beta, which is reliable and free on the Inference API
        self.hf_model_id = os.getenv("HUGGINGFACE_MODEL_ID", "HuggingFaceH4/zephyr-7b-beta")
        
        self.gemini_model = None
        self.openai_client = None
        self.hf_client = None
        
        # Initialize OpenAI if key exists
        if self.openai_api_key:
            self.openai_client = OpenAI(api_key=self.openai_api_key)
            
        # Initialize Hugging Face Client if key exists
        if self.huggingface_api_key:
             self.hf_client = InferenceClient(token=self.huggingface_api_key)

    def _init_gemini(self):
        """Lazy initialization check."""
        if not self.google_api_key:
             # Just warn, don't raise here to allow other providers
             print("Warning: GOOGLE_API_KEY not found in environment")

    def get_completion(self, system_prompt: str, user_prompt: str, json_mode: bool = False) -> str:
        # Priority: Gemini -> Hugging Face -> OpenAI
        
        # 1. Try Google Gemini (User preferred, waiting for quota reset)
        if self.google_api_key:
            try:
                self._init_gemini()
                return self._call_gemini(system_prompt, user_prompt, json_mode)
            except Exception as e:
                print(f"Gemini failed (quota might be exceeded), trying fallbacks: {e}")
        
        # 2. Try Hugging Face (Secondary free option)
        if self.hf_client:
            try:
                return self._call_huggingface(system_prompt, user_prompt, json_mode)
            except Exception as e:
                print(f"Hugging Face Inference failed: {e}")
        
        # 3. Try OpenAI
        if self.openai_client:
            return self._call_openai(system_prompt, user_prompt, json_mode)
            
        raise ValueError("No working API keys found. Please provide GOOGLE_API_KEY, HUGGINGFACE_API_KEY, or OPENAI_API_KEY in .env")

    def _call_huggingface(self, system_prompt: str, user_prompt: str, json_mode: bool) -> str:
        print(f"Calling Hugging Face Inference API with model: {self.hf_model_id}")
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        if json_mode:
            messages.append({"role": "user", "content": "Return the output ONLY as a valid JSON object."})

        try:
            # We use chat_completion for chat models
            response = self.hf_client.chat_completion(
                model=self.hf_model_id,
                messages=messages,
                max_tokens=4096,
                temperature=0.1,
                stream=False
            )
            return response.choices[0].message.content
        except Exception as e:
            # Fallback for models not supporting chat_completion (text-generation endpoint)
            # But Qwen-Coder-Instruct supports chat. 
            print(f"HF Chat Completion failed: {e}")
            raise e

    def _call_gemini(self, system_prompt: str, user_prompt: str, json_mode: bool) -> str:
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]
        
        if json_mode:
            messages.append(HumanMessage(content="Return the output ONLY as a valid JSON object."))
            
        # List of models to try in order of preference/stability
        # 1.5 Flash is efficient
        # 1.5 Pro is more capable
        # gemini-pro is legacy stable
        models_to_try = [
            "gemini-1.5-flash",
            "gemini-1.5-pro",
            "gemini-pro"
        ]
        
        last_error = None
        
        for model_name in models_to_try:
            try:
                print(f"Trying Gemini model: {model_name}...")
                llm = ChatGoogleGenerativeAI(
                    model=model_name,
                    google_api_key=self.google_api_key,
                    temperature=0,
                    convert_system_message_to_human=True
                )
                response = llm.invoke(messages)
                return response.content
            except Exception as e:
                print(f"Model {model_name} failed: {e}")
                last_error = e
                # Continue to next model
                continue
                
        if last_error:
            raise last_error
        return ""

    def _call_openai(self, system_prompt: str, user_prompt: str, json_mode: bool) -> str:
        response = self.openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            response_format={"type": "json_object"} if json_mode else None,
        )
        return response.choices[0].message.content
