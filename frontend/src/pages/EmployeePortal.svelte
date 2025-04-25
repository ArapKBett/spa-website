<script>
  import axios from 'axios';
  import { onMount } from 'svelte';
  let paystubs = [];
  let availability = {};
  let message = '';
  let error = '';

  async function fetchPaystubs() {
    try {
      const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/paystubs/`);
      paystubs = response.data;
    } catch (err) {
      console.error('Failed to fetch paystubs:', err);
    }
  }

  async function updateAvailability() {
    try {
      const response = await axios.post(`${import.meta.env.VITE_API_URL}/api/availability/`, {
        availability
      });
      message = 'Availability updated successfully!';
      error = '';
    } catch (err) {
      error = 'Failed to update availability. Please try again.';
      message = '';
    }
  }

  onMount(() => {
    fetchPaystubs();
    return () => {};
  });
</script>

<section class="py-12 px-4 max-w-6xl mx-auto">
  <h1 class="text-3xl font-bold mb-8">Employee Portal</h1>
  <h2 class="text-2xl font-bold mb-4">Paystubs</h2>
  {#if paystubs.length > 0}
    <ul class="list-disc pl-6">
      {#each paystubs as paystub}
        <li>Date: {paystub.date} - Amount: ${paystub.amount}</li>
      {/each}
    </ul>
  {:else}
    <p>No paystubs available.</p>
  {/if}

  <h2 class="text-2xl font-bold mt-8 mb-4">Update Availability</h2>
  <form on:submit|preventDefault={updateAvailability} class="flex flex-col gap-4 max-w-md">
    <input
      type="text"
      bind:value={availability.monday}
      placeholder="Monday availability (e.g., 9AM-5PM)"
      class="p-2 rounded text-black"
    />
    <button type="submit" class="bg-spaGold text-white p-2 rounded hover:bg-opacity-90">
      Update Availability
    </button>
  </form>
  {#if message}
    <p class="text-green-400 mt-4">{message}</p>
  {/if}
  {#if error}
    <p class="text-red-400 mt-4">{error}</p>
  {/if}
</section>

<svelte:head>
  <title>Employee Portal - Spa Serenity</title>
</svelte:head>
