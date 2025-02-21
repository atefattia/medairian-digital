import os
from pathlib import Path
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai import OpenAI
import logging

class RAGChatbot:
    def __init__(self, content_dir='content', max_context_length=1000):
        """
        Initialize RAG Chatbot with OpenAI ChatGPT 3.5 Turbo and Hugging Face Embeddings
        
        :param content_dir: Directory containing knowledge base documents
        :param max_context_length: Maximum length of context to include in response
        """
        # Configure logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Validate OpenAI API key
        openai_api_key = os.getenv('OPENAI_API_KEY')
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        
        self.max_context_length = max_context_length
        
        try:
            # Initialize small Hugging Face embeddings model
            embed_model = HuggingFaceEmbedding(
                model_name="BAAI/bge-small-en-v1.5",  # Lightweight, high-performance model
                cache_folder=Path(__file__).parent / ".embedding_cache"
            )
            
            # Initialize OpenAI ChatGPT 3.5 Turbo
            llm = OpenAI(
                model="gpt-3.5-turbo",
                temperature=0.1,
                max_tokens=256,
                api_key=openai_api_key
            )
            
            # Load documents from content directory
            documents = SimpleDirectoryReader(
                input_dir=content_dir, 
                recursive=True, 
                required_exts=['.yaml', '.yml', '.md']
            ).load_data()
            
            self.logger.info(f"Loaded {len(documents)} documents from {content_dir}")
            
            # Create vector index with Hugging Face embeddings
            self.index = VectorStoreIndex.from_documents(
                documents, 
                embed_model=embed_model,
                show_progress=True
            )
            
            # Create query engine with OpenAI LLM and Hugging Face embeddings
            self.query_engine = self.index.as_query_engine(
                llm=llm,
                embed_model=embed_model,
                similarity_top_k=3,  # Return top 3 most relevant context chunks
                response_mode='compact'
            )
            
            self.logger.info(f"Initialized RAG Chatbot with {len(documents)} documents using OpenAI ChatGPT 3.5 Turbo and Hugging Face embeddings")
        
        except Exception as e:
            self.logger.error(f"Error initializing RAG Chatbot: {e}")
            raise
    
    def _truncate_context(self, context: str) -> str:
        """
        Truncate context to prevent exceeding token limits
        
        :param context: Original context
        :return: Truncated context
        """
        return context[:self.max_context_length]
    
    def generate_response(self, query: str) -> str:
        """
        Generate a professional and context-aware response using OpenAI ChatGPT
        
        :param query: User's input query
        :return: AI-generated response
        """
        try:
            # Retrieve context-aware response
            response = self.query_engine.query(query)
            processed_response = str(response)
            
            # Truncate and process response
            processed_response = self._truncate_context(processed_response)
            
            # Log interaction
            self.logger.info(f"Query: {query} | Response Length: {len(processed_response)}")
            
            return processed_response
        
        except Exception as e:
            error_msg = f" Apologies, I encountered an issue processing your request. {str(e)}"
            self.logger.error(error_msg)
            return error_msg


if __name__ == "__main__":
    chatbot = RAGChatbot()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = chatbot.generate_response(user_input)
        print("Medairian: ", response)