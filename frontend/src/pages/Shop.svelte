<script>
  import { onMount } from 'svelte';
  import axios from 'axios';
  import { loadStripe } from '@stripe/stripe-js';
  let products = [];
  let cart = [];

  onMount(async () => {
    const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/products/`);
    products = response.data;
  });

  async function checkout() {
    const stripe = await loadStripe('your-stripe-publishable-key');
    const response = await axios.post(`${import.meta.env.VITE_API_URL}/api/checkout/`, { order_id: 1 }, { // Replace with dynamic order ID
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    });
    stripe.redirectToCheckout({ sessionId: response.data.sessionId });
  }
</script>

<div class="p-8">
  <h2 class="text-2xl mb-4">Shop Our Products</h2>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
    {#each products as product}
      <div class="p-4 border rounded-md">
        <img src={product.image} alt={product.name} class="w-full h-48 object-cover" />
        <h3>{product.name}</h3>
        <p>${product.price}</p>
        <button on:click={() => cart = [...cart, product]} class="bg-spaGold text-white p-2">Add to Cart</button>
      </div>
    {/each}
  </div>
  {#if cart.length}
    <button on:click={checkout} class="bg-spaGold text-white p-2 mt-4">Checkout</button>
  {/if}
</div>
