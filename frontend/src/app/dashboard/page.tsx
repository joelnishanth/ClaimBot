import ListingCard from '../../components/ListingCard';

const mockListings = [
  { id: 1, title: 'Sample Item 1', imageUrl: '/placeholder.png', similarity: 0.92 },
  { id: 2, title: 'Sample Item 2', imageUrl: '/placeholder.png', similarity: 0.88 },
];

export default function Dashboard() {
  return (
    <main className="p-4 grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
      {mockListings.map((listing) => (
        <ListingCard key={listing.id} listing={listing} />
      ))}
    </main>
  );
}
