<template>
  <div class="record-form">
    <h2>Add New Record</h2>
    <form @submit.prevent="submitForm">
      <input v-model="record.first_name" placeholder="First Name" required>
      <input v-model="record.last_name" placeholder="Last Name" required>
      <input v-model="record.phone" placeholder="Phone" required>
      <input v-model="record.city" placeholder="City" required>
      <button type="submit">Add Record</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = import.meta.env.VITE_BACKEND_URL

export default {
  name: 'RecordForm',
  data() {
    return {
      record: {
        first_name: '',
        last_name: '',
        phone: '',
        city: ''
      }
    };
  },
  methods: {
    async submitForm() {
      try {
        await axios.post(`${API_URL}/records`, this.record);
        this.$emit('record-added');
        this.resetForm();
      } catch (error) {
        console.error('Error adding record:', error);
      }
    },
    resetForm() {
      this.record = {
        first_name: '',
        last_name: '',
        phone: '',
        city: ''
      };
    }
  }
};
</script>

<style scoped>
h2 {
  color: black;
}
.record-form {
  background-color: #f9f9f9;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Limit the form width and make it centered */
form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-width: 500px;
  margin: 0 auto;
}

input {
  padding: 10px;
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
</style>
