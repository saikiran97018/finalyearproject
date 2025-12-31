class Certificate:
    """In-memory certificate storage (replace with database in production)"""
    
    def __init__(self):
        self.certificates = {}
    
    def create(self, certificate_data, quantum_hash):
        """Create and store a new certificate"""
        certificate = {
            **certificate_data,
            'quantumHash': quantum_hash['hash'],
            'timestamp': quantum_hash['timestamp'],
            'algorithm': quantum_hash['algorithm'],
            'status': 'valid'
        }
        
        self.certificates[certificate_data['certificateId']] = certificate
        return certificate
    
    def find_by_id(self, certificate_id):
        """Find certificate by ID"""
        return self.certificates.get(certificate_id)
    
    def get_all(self):
        """Get all certificates"""
        return list(self.certificates.values())

# Global instance
certificate_store = Certificate()