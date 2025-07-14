'use client';
import { useState } from 'react';

export default function Submit() {
  const [form, setForm] = useState({ shopUrl: '', title: '', description: '', imageUrl: '' });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: submit to backend
    alert('Submitted');
  };

  return (
    <main className="p-4 max-w-xl mx-auto">
      <form onSubmit={handleSubmit} className="space-y-4">
        <input name="shopUrl" placeholder="Shop URL" className="w-full p-2 rounded border" onChange={handleChange} />
        <input name="title" placeholder="Title" className="w-full p-2 rounded border" onChange={handleChange} />
        <textarea name="description" placeholder="Description" className="w-full p-2 rounded border" onChange={handleChange} />
        <input name="imageUrl" placeholder="Image URL" className="w-full p-2 rounded border" onChange={handleChange} />
        <button type="submit" className="px-4 py-2 bg-black text-white rounded">Submit</button>
      </form>
    </main>
  );
}
