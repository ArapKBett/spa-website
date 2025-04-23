<script>
  import axios from 'axios';
  let name = '';
  let email = '';
  let message = '';
  let responseMessage = '';

  async function handleSubmit() {
    try {
      const response = await axios.post(`${import.meta.env.VITE_API_URL}/api/contact/`, { name, email, message });
      responseMessage = response.data.message;
      name = email = message = '';
    } catch (error) {
      responseMessage = 'Error sending message.';
    }
  }
</script>

<form on:submit|preventDefault={handleSubmit} class="flex flex-col gap-4 max-w-md mx-auto">
  <input type="text" bind:value={name} placeholder="Name" class="p-2 rounded-md border text-spaNavy" required />
  <input type="email" bind:value={email} placeholder="Email" class="p-2 rounded-md border text-spaNavy" required />
  <textarea bind:value={message} placeholder="Message" class="p-2 rounded-md border text-spaNavy" required></textarea>
  <button type="submit" class="bg-spaGold text-white p-2 rounded-md">Send</button>
  {#if responseMessage}
    <p>{responseMessage}</p>
  {/if}
</form>
