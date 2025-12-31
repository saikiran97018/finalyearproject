
const API_URL = 'http://localhost:5000/api/certificates';

// Tab switching functionality
function showTab(tabName) {
  const tabs = document.querySelectorAll('.tab-content');
  const btns = document.querySelectorAll('.tab-btn');
  
  tabs.forEach(tab => tab.classList.remove('active'));
  btns.forEach(btn => btn.classList.remove('active'));
  
  document.getElementById(`${tabName}-tab`).classList.add('active');
  event.target.classList.add('active');

  if (tabName === 'view') {
    loadAllCertificates();
  }
}

// Issue Certificate Form Handler
document.getElementById('issue-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const certificateData = {
    certificateId: document.getElementById('issue-id').value,
    holderName: document.getElementById('issue-name').value,
    course: document.getElementById('issue-course').value,
    issueDate: document.getElementById('issue-date').value
  };

  try {
    const response = await fetch(`${API_URL}/issue`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(certificateData)
    });

    const data = await response.json();
    const resultDiv = document.getElementById('issue-result');

    if (data.success) {
      resultDiv.className = 'result success';
      resultDiv.innerHTML = `
        ✅ Certificate Issued Successfully!
        Certificate ID: ${data.certificate.certificateId}
        Holder: ${data.certificate.holderName}
        Course: ${data.certificate.course}
        Issue Date: ${data.certificate.issueDate}
        
          Quantum Hash:
          ${data.certificate.quantumHash}
        
        Algorithm: ${data.certificate.algorithm}
        Timestamp: ${new Date(data.certificate.timestamp).toLocaleString()}
      `;
      document.getElementById('issue-form').reset();
    } else {
      resultDiv.className = 'result error';
      resultDiv.innerHTML = `❌ Error${data.message}`;
    }
  } catch (error) {
    const resultDiv = document.getElementById('issue-result');
    resultDiv.className = 'result error';
    resultDiv.innerHTML = `
      ❌ Connection Error
      Could not connect to the server. Please ensure the Flask backend is running on port 5000.
      Error: ${error.message}
    `;
  }
});

// Verify Certificate Form Handler
document.getElementById('verify-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const certificateData = {
    certificateId: document.getElementById('verify-id').value,
    holderName: document.getElementById('verify-name').value,
    course: document.getElementById('verify-course').value,
    issueDate: document.getElementById('verify-date').value
  };

  try {
    const response = await fetch(`${API_URL}/verify`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(certificateData)
    });

    const data = await response.json();
    const resultDiv = document.getElementById('verify-result');

    if (data.isValid) {
      resultDiv.className = 'result success';
      resultDiv.innerHTML = `
        ✅ AUTHENTIC CERTIFICATE
        ${data.message}
        
          Verification Details:
          ✓ Quantum Hash Match: ${data.verificationDetails.hashMatch ? 'PASS ✅' : 'FAIL ❌'}
          ✓ Data Integrity: ${data.verificationDetails.dataMatch ? 'PASS ✅' : 'FAIL ❌'}
          ✓ Algorithm: ${data.verificationDetails.algorithm}
        
        
          Original Certificate Details:
          Holder: ${data.originalData.holderName}
          Course: ${data.originalData.course}
          Issue Date: ${data.originalData.issueDate}
        
      `;
    } else {
      resultDiv.className = 'result error';
      resultDiv.innerHTML = `
        ⚠️ FAKE CERTIFICATE DETECTED
        ${data.message}
        
          Warning:
          ${data.reason || 'The certificate data does not match our records or has been tampered with.'}
          ${data.verificationDetails ? `
            Hash Match: ${data.verificationDetails.hashMatch ? '✓' : '✗'}
            Data Match: ${data.verificationDetails.dataMatch ? '✓' : '✗'}
          ` : ''}
        
      `;
    }
  } catch (error) {
    const resultDiv = document.getElementById('verify-result');
    resultDiv.className = 'result error';
    resultDiv.innerHTML = `
      ❌ Connection Error
      Could not connect to the server. Please ensure the Flask backend is running on port 5000.
      Error: ${error.message}
    `;
  }
});

// Load All Certificates
async function loadAllCertificates() {
  const listDiv = document.getElementById('certificates-list');
  listDiv.innerHTML = '⏳ Loading certificates...';

  try {
    const response = await fetch(`${API_URL}/all`);
    const data = await response.json();

    if (data.certificates.length === 0) {
      listDiv.innerHTML = `
        
          📄
          No certificates issued yet
          Use the "Issue Certificate" tab to create your first certificate
        
      `;
      return;
    }

    listDiv.innerHTML = `
      
        Total Certificates: ${data.count}
      
    ` + data.certificates.map(cert => `
      
        📜 Certificate: ${cert.certificateId}
        Holder: ${cert.holderName}
        Course: ${cert.course}
        Issue Date: ${cert.issueDate}
        Status: ✓ ${cert.status.toUpperCase()}
        Algorithm: ${cert.algorithm}
        
          Quantum Hash:
          ${cert.quantumHash}
        
        
          Timestamp: ${new Date(cert.timestamp).toLocaleString()}
        
      
    `).join('');
  } catch (error) {
    listDiv.innerHTML = `
      
        ❌ Connection Error
        Could not load certificates. Please ensure the Flask backend is running on port 5000.
        Error: ${error.message}
      
    `;
  }
}

// Set today's date as default
const today = new Date().toISOString().split('T')[0];
document.getElementById('issue-date').value = today;
document.getElementById('verify-date').value = today;

// Initial message
console.log('Quantum Certificate Verification System Loaded');
console.log('Backend API URL:', API_URL);