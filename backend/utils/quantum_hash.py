import hashlib
import time
import json

class QuantumHash:
    """Simulate quantum-resistant hash generation and verification"""
    
    @staticmethod
    def generate(data):
        """Generate a quantum-resistant hash from certificate data"""
        # Convert data to string if it's a dictionary
        if isinstance(data, dict):
            data = json.dumps(data, sort_keys=True)
        
        # Combine multiple hash algorithms to simulate quantum resistance
        sha256_hash = hashlib.sha256(data.encode()).hexdigest()
        sha512_hash = hashlib.sha512(data.encode()).hexdigest()
        
        # Simulate quantum entanglement by mixing hashes
        combined = sha256_hash + sha512_hash + str(time.time())
        quantum_hash = hashlib.sha256(combined.encode()).hexdigest()
        
        return {
            'hash': quantum_hash,
            'timestamp': int(time.time() * 1000),
            'algorithm': 'QUANTUM-SHA-512'
        }
    
    @staticmethod
    def regenerate(certificate_data):
        """Regenerate quantum hash for verification"""
        # Create deterministic data string
        data_dict = {
            'holderName': certificate_data.get('holderName'),
            'certificateId': certificate_data.get('certificateId'),
            'issueDate': certificate_data.get('issueDate'),
            'course': certificate_data.get('course')
        }
        
        data_string = json.dumps(data_dict, sort_keys=True)
        
        sha256_hash = hashlib.sha256(data_string.encode()).hexdigest()
        sha512_hash = hashlib.sha512(data_string.encode()).hexdigest()
        
        combined = sha256_hash + sha512_hash
        regenerated_hash = hashlib.sha256(combined.encode()).hexdigest()
        
        return regenerated_hash
    
    @staticmethod
    def verify(original_hash, certificate_data):
        """Verify if hashes match"""
        regenerated_hash = QuantumHash.regenerate(certificate_data)
        # Compare first 32 characters for partial matching
        return original_hash[:32] == regenerated_hash[:32]