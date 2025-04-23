<script>
  import axios from 'axios';
  let username = '';
  let password = '';
  let error = '';

  async function handleLogin() {
    try {
      const response = await axios.post(`${import.meta.env.VITE_API_URL}/api/token/`, { username, password });
      localStorage.setItem('token', response.data.access);
      window.location.href = '/dashboard';
    } catch (err) {
      error = 'Invalid credentials';
    }
  }
</script>

<form on:submit|preventDefault={handleLogin} class="flex flex-col gap-4 max-w-md mx-auto">
  <input type="text" bind:value={username} placeholder="Username" class="p-2 rounded-md border text-spaNavy" required />
  <input type="password" bind:value={password} placeholder="Password" class="p-2 rounded-md border text-spaNavy" required />
  <button type="submit" class="bg-spaGold text-white p-2 rounded-md">Login</button>
  {#if error}
    <p>{error}</p>
  {/if}
</form>
