const API_BASE = 'http://localhost:8001';

const api = {
  async getGithubAuthUrl() {
    try {
      const response = await fetch(`${API_BASE}/auth/github`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    } catch (error) {
      if (error.message.includes('Failed to fetch')) {
        throw new Error('Cannot connect to backend. Make sure the backend is running on http://localhost:8001');
      }
      throw error;
    }
  },

  async getUserProfile() {
    const token = localStorage.getItem('access_token');
    const response = await fetch(`${API_BASE}/api/profile`, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    if (!response.ok) throw new Error('Failed to fetch profile');
    return response.json();
  },

  async getUserRepos() {
    const token = localStorage.getItem('access_token');
    try {
      const response = await fetch(`${API_BASE}/api/profile/repos`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      if (!response.ok) {
        const error = await response.text();
        console.error('Failed to fetch repos:', response.status, error);
        throw new Error('Failed to fetch repos');
      }
      return response.json();
    } catch (error) {
      console.error('Error fetching repos:', error);
      throw error;
    }
  },

  async cloneRepository(data) {
    const token = localStorage.getItem('access_token');
    const response = await fetch(`${API_BASE}/api/profile/clone`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(data)
    });
    if (!response.ok) throw new Error('Failed to clone repository');
    return response.json();
  },

  async getClonedRepos() {
    const token = localStorage.getItem('access_token');
    const response = await fetch(`${API_BASE}/api/profile/cloned`, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    if (!response.ok) throw new Error('Failed to fetch cloned repos');
    return response.json();
  },

  async removeClonedRepo(repoName) {
    const token = localStorage.getItem('access_token');
    const response = await fetch(`${API_BASE}/api/profile/cloned/${repoName}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    if (!response.ok) throw new Error('Failed to remove repository');
    return response.json();
  },

  async saveFixedBranch(data) {
    const token = localStorage.getItem('access_token');
    const response = await fetch(`${API_BASE}/api/profile/fixed-branch`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(data)
    });
    if (!response.ok) throw new Error('Failed to save fixed branch');
    return response.json();
  },

  async getFixedBranches() {
    const token = localStorage.getItem('access_token');
    const response = await fetch(`${API_BASE}/api/profile/fixed-branches`, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    if (!response.ok) throw new Error('Failed to fetch fixed branches');
    return response.json();
  },

  async removeFixedBranch(branchName) {
    const token = localStorage.getItem('access_token');
    const response = await fetch(`${API_BASE}/api/profile/fixed-branch/${branchName}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    if (!response.ok) throw new Error('Failed to remove fixed branch');
    return response.json();
  }
};

export default api;