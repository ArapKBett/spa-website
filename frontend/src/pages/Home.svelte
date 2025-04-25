<script>
  import axios from 'axios';
  import { onMount } from 'svelte';
  import SubscribeForm from '../components/SubscribeForm.svelte';
  let specials = [];

  async function fetchSpecials() {
    try {
      const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/specials/`);
      specials = response.data;
    } catch (err) {
      console.error('Failed to fetch specials:', err);
    }
  }

  onMount(() => {
    fetchSpecials();
    return () => {};
  });
</script>

<section class="py-12 px-4 max-w-6xl mx-auto">
  <h1 class="text-4xl font-bold text-center mb-8">Spa Serenity</h1>
  <p class="text-center mb-12">Welcome to our luxurious spa. Discover our services and specials!</p>

  {#if specials.length > 0}
    <h2 class="text-2xl font-bold mb-4">Special Offers</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {#each specials as special}
        <div class="bg-white text-black p-4 rounded shadow">
          <h3 class="text-xl font-bold">{special.title}</h3>
          <p>{special.description}</p>
          {#if special.image}
            <img src={special.image} alt={special.title} class="mt-2 w-full h-48 object-cover" />
          {/if}
        </div>
      {/each}
    </div>
  {/if}

  <h2 class="text-2xl font-bold mt-12 mb-4">Subscribe to Our Newsletter</h2>
  <SubscribeForm />
</section>

<svelte:head>
  <title>Home - Spa Serenity</title>
</svelte:head>
