from cryptography.fernet import Fernet
import os


class TokenService:
    """Encrypt/decrypt tokens, refresh logic."""
    
    @staticmethod
    def get_key():
        """Get encryption key from environment or generate one."""
        key = os.environ.get('TOKEN_ENCRYPTION_KEY')
        if not key:
            key = Fernet.generate_key()
        return key if isinstance(key, bytes) else key.encode()
    
    @staticmethod
    def get_cipher():
        """Get Fernet cipher instance."""
        return Fernet(TokenService.get_key())
    
    @staticmethod
    def encrypt_token(token):
        """Encrypt a token."""
        cipher = TokenService.get_cipher()
        return cipher.encrypt(token.encode()).decode()
    
    @staticmethod
    def decrypt_token(encrypted_token):
        """Decrypt a token."""
        cipher = TokenService.get_cipher()
        return cipher.decrypt(encrypted_token.encode()).decode()
    
    @staticmethod
    def is_token_expired(expires_at):
        """Check if token is expired."""
        from datetime import datetime
        return datetime.utcnow() > expires_at
