<script>
  import axios from 'axios';
  import { onMount } from 'svelte';
  import { Calendar } from '@fullcalendar/core';
  import dayGridPlugin from '@fullcalendar/daygrid';
  import timeGridPlugin from '@fullcalendar/timegrid';
  let calendarEl;
  let services = [];
  let employees = [];
  let selectedService = '';
  let selectedEmployee = '';
  let message = '';
  let error = '';

  async function fetchData() {
    try {
      const [servicesRes, employeesRes] = await Promise.all([
        axios.get(`${import.meta.env.VITE_API_URL}/api/services/`),
        axios.get(`${import.meta.env.VITE_API_URL}/api/employees/`)
      ]);
      services = servicesRes.data;
      employees = employeesRes.data;
      if (services.length > 0) selectedService = services[0].id;
      if (employees.length > 0) selectedEmployee = employees[0].id;
    } catch (err) {
      console.error('Failed to fetch data:', err);
    }
  }

  async function handleBooking(event) {
    try {
      const response = await axios.post(`${import.meta.env.VITE_API_URL}/api/bookings/`, {
        service: selectedService,
        employee: selectedEmployee,
        start_time: event.startStr,
        end_time: event.endStr
      });
      message = 'Booking created successfully!';
      error = '';
    } catch (err) {
      error = 'Failed to create booking. Please try again.';
      message = '';
    }
  }

  onMount(() => {
    fetchData();
    const calendar = new Calendar(calendarEl, {
      plugins: [dayGridPlugin, timeGridPlugin],
      initialView: 'timeGridWeek',
      selectable: true,
      select: handleBooking
    });
    calendar.render();
    return () => calendar.destroy();
  });
</script>

<section class="py-12 px-4 max-w-6xl mx-auto">
  <h1 class="text-3xl font-bold mb-8">Book an Appointment</h1>
  <div class="mb-8">
    <label for="service" class="block mb-2">Select Service:</label>
    <select bind:value={selectedService} id="service" class="p-2 rounded text-black">
      {#each services as service}
        <option value={service.id}>{service.name}</option>
      {/each}
    </select>
  </div>
  <div class="mb-8">
    <label for="employee" class="block mb-2">Select Employee:</label>
    <select bind:value={selectedEmployee} id="employee" class="p-2 rounded text-black">
      {#each employees as employee}
        <option value={employee.id}>{employee.user.username}</option>
      {/each}
    </select>
  </div>
  <div bind:this={calendarEl}></div>
  {#if message}
    <p class="text-green-400 mt-4">{message}</p>
  {/if}
  {#if error}
    <p class="text-red-400 mt-4">{error}</p>
  {/if}
</section>

<svelte:head>
  <title>Booking - Spa Serenity</title>
</svelte:head>
