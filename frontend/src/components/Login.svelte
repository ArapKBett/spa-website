<script>
  import axios from 'axios';
  let username = '';
  let password = '';
  let error = '';
  let success = '';

  async function handleLogin() {
    try {
      const response = await axios.post(`${import.meta.env.VITE_API_URL}/api/login/`, {
        username,
        password
      });
      success = 'Login successful!';
      error = '';
      // Store token or redirect as needed
    } catch (err) {
      error = 'Invalid credentials. Please try again.';
      success = '';
    }
  }
</script>

<form on:submit|preventDefault={handleLogin} class="flex flex-col gap-4 max-w-md mx-auto">
  <input
    type="text"
    bind:value={username}
    placeholder="Username"
    required
    class="p-2 rounded text-black"
  />
  <input
    type="password"
    bind:value={password}
    placeholder="Password"
    required
    class="p-2 rounded text-black"
  />
  <button type="submit" class="bg-spaGold text-white p-2 rounded hover:bg-opacity-90">
    Login
  </button>
  {#if success}
    <p class="text-green-400">{success}</p>
  {/if}
  {#if error}
    <p class="text-red-400">{error}</p>
  {/if}
</form>
