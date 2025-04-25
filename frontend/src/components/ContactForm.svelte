<script>
  import axios from 'axios';
  let name = '';
  let email = '';
  let message = '';
  let success = '';
  let error = '';

  async function handleSubmit() {
    try {
      const response = await axios.post(`${import.meta.env.VITE_API_URL}/api/contact/`, {
        name,
        email,
        message
      });
      success = 'Message sent successfully!';
      error = '';
      name = '';
      email = '';
      message = '';
    } catch (err) {
      error = 'Failed to send message. Please try again.';
      success = '';
    }
  }
</script>

<form on:submit|preventDefault={handleSubmit} class="flex flex-col gap-4 max-w-md mx-auto">
  <input
    type="text"
    bind:value={name}
    placeholder="Your Name"
    required
    class="p-2 rounded text-black"
  />
  <input
    type="email"
    bind:value={email}
    placeholder="Your Email"
    required
    class="p-2 rounded text-black"
  />
  <textarea
    bind:value={message}
    placeholder="Your Message"
    required
    class="p-2 rounded text-black h-32"
  ></textarea>
  <button type="submit" class="bg-spaGold text-white p-2 rounded hover:bg-opacity-90">
    Send Message
  </button>
  {#if success}
    <p class="text-green-400">{success}</p>
  {/if}
  {#if error}
    <p class="text-red-400">{error}</p>
  {/if}
</form>
