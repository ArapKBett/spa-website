<script>
  import { onMount } from 'svelte';
  import axios from 'axios';
  let availability = { monday: '', tuesday: '', wednesday: '', thursday: '', friday: '' };
  let paystubs = [];

  onMount(async () => {
    const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/paystubs/`, {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    });
    paystubs = response.data;
  });

  async function updateAvailability() {
    try {
      await axios.post(`${import.meta.env.VITE_API_URL}/api/availability/`, { availability }, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
      });
      alert('Availability updated');
    } catch (error) {
      alert('Error updating availability');
    }
  }
</script>

<div class="p-8">
  <h2 class="text-2xl mb-4">Employee Portal</h2>
  <h3 class="mb-2">Update Availability</h3>
  <div class="flex flex-col gap-4 max-w-md">
    <input type="text" bind:value={availability.monday} placeholder="Monday (e.g., 9:00-17:00)" class="p-2 rounded-md border text-spaNavy" />
    <input type="text" bind:value={availability.tuesday} placeholder="Tuesday" class="p-2 rounded-md border text-spaNavy" />
    <input type="text" bind:value={availability.wednesday} placeholder="Wednesday" class="p-2 rounded-md border text-spaNavy" />
    <input type="text" bind:value={availability.thursday} placeholder="Thursday" class="p-2 rounded-md border text-spaNavy" />
    <input type="text" bind:value={availability.friday} placeholder="Friday" class="p-2 rounded-md border text-spaNavy" />
    <button on:click={updateAvailability} class="bg-spaGold text-white p-2 rounded-md">Update</button>
  </div>
  <h3 class="mt-6 mb-2">Paystubs</h3>
  {#each paystubs as stub}
    <p>{stub.date} - ${stub.amount}</p>
  {/each}
</div>
