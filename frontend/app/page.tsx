'use client';

import { useState } from 'react';

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [trolledCV, setTrolledCV] = useState<any>(null);
  const [error, setError] = useState<string>('');

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
      setError('');
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!file) return;

    setLoading(true);
    setError('');
    setTrolledCV(null);
    
    const formData = new FormData();
    formData.append('file', file);

    try {
      const apiUrl = '/api/troll_cv';
      
      const response = await fetch(apiUrl, {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setTrolledCV(data);
    } catch (error: any) {
      console.error('Error:', error);
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-purple-500 to-pink-500 p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-5xl font-bold text-white text-center mb-4">
          CV Troll Malayalam 😂
        </h1>
        <p className="text-white text-center mb-8">
          Upload your CV and get roasted in Malayalam!
        </p>

        <div className="bg-white rounded-lg shadow-xl p-8">
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-gray-700 font-semibold mb-2">
                Upload CV (PDF or DOCX)
              </label>
              <input
                type="file"
                accept=".pdf,.doc,.docx"
                onChange={handleFileChange}
                className="w-full px-4 py-2 border-2 border-gray-300 rounded-lg focus:border-purple-500 focus:outline-none"
                required
              />
            </div>

            <button
              type="submit"
              disabled={loading || !file}
              className="w-full bg-purple-600 hover:bg-purple-700 text-white font-bold py-3 px-6 rounded-lg disabled:opacity-50 disabled:cursor-not-allowed transition"
            >
              {loading ? '🔄 Trolling Your CV...' : 'Troll My CV! 🤣'}
            </button>
          </form>

          {error && (
            <div className="mt-4 p-4 bg-red-100 border border-red-400 text-red-700 rounded-lg">
              <strong>Error:</strong> {error}
            </div>
          )}

          {loading && (
            <div className="mt-8 text-center">
              <div className="animate-spin rounded-full h-16 w-16 border-b-4 border-purple-600 mx-auto"></div>
              <p className="mt-4 text-gray-600">Processing your CV...</p>
            </div>
          )}

          {trolledCV && trolledCV.success && (
            <div className="mt-8 space-y-6">
              <h2 className="text-3xl font-bold text-purple-600 text-center mb-6">
                😂 Your CV Got Roasted! 😂
              </h2>
              
              {trolledCV.trolled_sections && trolledCV.trolled_sections.length > 0 ? (
                trolledCV.trolled_sections.map((section: any, idx: number) => (
                  <div 
                    key={idx} 
                    className="bg-purple-50 border-l-4 border-purple-500 rounded-lg p-6 shadow-md hover:shadow-lg transition"
                  >
                    <h3 className="text-xl font-bold text-gray-800 mb-3">
                      📌 {section.title}
                    </h3>
                    <div className="bg-white p-4 rounded-md">
                      <p className="text-2xl text-purple-700 leading-relaxed">
                        {section.troll}
                      </p>
                    </div>
                  </div>
                ))
              ) : (
                <div className="text-center text-gray-600">
                  <p>No sections found to troll! 🤔</p>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </main>
  );
}
