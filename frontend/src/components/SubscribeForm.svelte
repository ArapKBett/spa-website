<script>
  import axios from 'axios';
  let email = '';
  let message = '';

  async function handleSubmit() {
    try {
      const response = await axios.post(`${import.meta.env.VITE_API_URL}/api/subscribe/`, { email });
      message = response.data.message;
      email = '';
    } catch (error) {
      message = 'Error subscribing. Please try again.';
    }
  }
</script>

<form on:submit|preventDefault={handleSubmit} class="flex flex-col gap-4 max-w-md mx-auto">
  <input
    type="email"
    bind:value={email}
    placeholder="Enter your email"
    class="p-2 rounded-md border border-spaNavy text-spaNavy"
    required
  />
  <button type="submit" class="bg-spaGold text-white p-2 rounded-md">Subscribe</button>
  {#if message}
    <p>{message}</p>
  {/if}
</form>
