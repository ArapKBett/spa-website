<script>
  import axios from 'axios';
  import { onMount } from 'svelte';
  import { loadStripe } from '@stripe/stripe-js';
  let products = [];
  let cart = [];
  let message = '';
  let error = '';

  async function fetchProducts() {
    try {
      const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/products/`);
      products = response.data;
    } catch (err) {
      console.error('Failed to fetch products:', err);
    }
  }

  function addToCart(product) {
    cart = [...cart, { ...product, quantity: 1 }];
  }

  async function checkout() {
    try {
      const stripe = await loadStripe('your-stripe-publishable-key');
      const response = await axios.post(`${import.meta.env.VITE_API_URL}/api/orders/`, {
        items: cart
      });
      const sessionId = response.data.session_id;
      await stripe.redirectToCheckout({ sessionId });
    } catch (err) {
      error = 'Failed to process checkout. Please try again.';
      message = '';
    }
  }

  onMount(() => {
    fetchProducts();
    return () => {};
  });
</script>

<section class="py-12 px-4 max-w-6xl mx-auto">
  <h1 class="text-3xl font-bold mb-8">Shop Our Products</h1>
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    {#each products as product}
      <div class="bg-white text-black p-4 rounded shadow">
        <h3 class="text-xl font-bold">{product.name}</h3>
        <p>${product.price}</p>
        {#if product.image}
          <img src={product.image} alt={product.name} class="mt-2 w-full h-48 object-cover" />
        {/if}
        <button
          on:click={() => addToCart(product)}
          class="bg-spaGold text-white p-2 mt-2 rounded hover:bg-opacity-90"
        >
          Add to Cart
        </button>
      </div>
    {/each}
  </div>
  {#if cart.length > 0}
    <div class="mt-8">
      <h2 class="text-2xl font-bold mb-4">Cart</h2>
      {#each cart as item}
        <p>{item.name} - ${item.price} x {item.quantity}</p>
      {/each}
      <button
        on:click={checkout}
        class="bg-spaGold text-white p-2 mt-4 rounded hover:bg-opacity-90"
      >
        Checkout
      </button>
    </div>
  {/if}
  {#if message}
    <p class="text-green-400 mt-4">{message}</p>
  {/if}
  {#if error}
    <p class="text-red-400 mt-4">{error}</p>
  {/if}
</section>

<svelte:head>
  <title>Shop - Spa Serenity</title>
</svelte:head>
