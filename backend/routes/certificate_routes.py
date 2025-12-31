from flask import Blueprint, request, jsonify
from models.certificate import certificate_store
from utils.quantum_hash import QuantumHash

certificate_bp = Blueprint('certificates', __name__)

@certificate_bp.route('/issue', methods=['POST'])
def issue_certificate():
    """Issue a new certificate with quantum hash"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['holderName', 'certificateId', 'course', 'issueDate']
        if not all(field in data for field in required_fields):
            return jsonify({
                'success': False,
                'message': 'All fields are required'
            }), 400
        
        # Check if certificate already exists
        if certificate_store.find_by_id(data['certificateId']):
            return jsonify({
                'success': False,
                'message': 'Certificate ID already exists'
            }), 409
        
        # Generate quantum hash
        quantum_hash = QuantumHash.generate(data)
        
        # Store certificate
        certificate = certificate_store.create(data, quantum_hash)
        
        return jsonify({
            'success': True,
            'message': 'Certificate issued successfully',
            'certificate': certificate
        }), 201
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Server error',
            'error': str(e)
        }), 500

@certificate_bp.route('/verify', methods=['POST'])
def verify_certificate():
    """Verify certificate authenticity using quantum hash"""
    try:
        data = request.get_json()
        
        if 'certificateId' not in data:
            return jsonify({
                'success': False,
                'message': 'Certificate ID is required'
            }), 400
        
        # Find original certificate
        original_certificate = certificate_store.find_by_id(data['certificateId'])
        
        if not original_certificate:
            return jsonify({
                'success': False,
                'message': 'Certificate not found',
                'isValid': False,
                'reason': 'Certificate does not exist in our records'
            }), 404
        
        # Verify quantum hash
        is_hash_valid = QuantumHash.verify(
            original_certificate['quantumHash'],
            data
        )
        
        # Verify data integrity
        data_match = (
            original_certificate['holderName'] == data.get('holderName') and
            original_certificate['course'] == data.get('course') and
            original_certificate['issueDate'] == data.get('issueDate')
        )
        
        is_valid = is_hash_valid and data_match
        
        return jsonify({
            'success': True,
            'isValid': is_valid,
            'message': 'Certificate is authentic' if is_valid else 'Certificate is FAKE - Hash mismatch or data tampering detected',
            'originalData': original_certificate,
            'verificationDetails': {
                'hashMatch': is_hash_valid,
                'dataMatch': data_match,
                'algorithm': original_certificate['algorithm']
            }
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Verification error',
            'error': str(e)
        }), 500

@certificate_bp.route('/all', methods=['GET'])
def get_all_certificates():
    """Get all issued certificates"""
    try:
        certificates = certificate_store.get_all()
        return jsonify({
            'success': True,
            'count': len(certificates),
            'certificates': certificates
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Server error',
            'error': str(e)
        }), 500