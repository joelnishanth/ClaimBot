export default function ListingCard({ listing }: { listing: { id: number; title: string; imageUrl: string; similarity: number } }) {
  return (
    <div className="bg-white rounded shadow p-4 hover:shadow-lg transition-transform hover:scale-105">
      <img src={listing.imageUrl} alt={listing.title} className="w-full h-48 object-cover rounded" />
      <h2 className="mt-2 font-semibold">{listing.title}</h2>
      <span className="text-sm text-gray-600">Similarity: {(listing.similarity * 100).toFixed(0)}%</span>
      <button className="mt-2 px-3 py-1 bg-blue-600 text-white rounded">Generate DMCA</button>
    </div>
  );
}
