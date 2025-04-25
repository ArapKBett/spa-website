<script>
  import axios from 'axios';
  let email = '';
  let message = '';
  let error = '';

  async function handleSubmit() {
    try {
      const response = await axios.post(`${import.meta.env.VITE_API_URL}/api/subscribers/`, { email });
      message = 'Thank you for subscribing!';
      error = '';
      email = '';
    } catch (err) {
      error = 'Failed to subscribe. Please try again.';
      message = '';
    }
  }
</script>

<form on:submit|preventDefault={handleSubmit} class="flex flex-col gap-4 max-w-md mx-auto">
  <input
    type="email"
    bind:value={email}
    placeholder="Enter your email"
    required
    class="p-2 rounded text-black"
  />
  <button type="submit" class="bg-spaGold text-white p-2 rounded hover:bg-opacity-90">
    Subscribe
  </button>
  {#if message}
    <p class="text-green-400">{message}</p>
  {/if}
  {#if error}
    <p class="text-red-400">{error}</p>
  {/if}
</form>
