<template>
  <div id="app">
    <div class="container">
      <h1>Records Management</h1>
      <record-form @record-added="fetchRecords"></record-form>
      <record-list :records="records" @record-updated="fetchRecords" @record-deleted="fetchRecords"></record-list>
    </div>
  </div>
</template>

<script>
import RecordForm from './components/RecordForm.vue';
import RecordList from './components/RecordList.vue';
import axios from 'axios';

export default {
  name: 'App',
  components: {
    RecordForm,
    RecordList
  },
  data() {
    return {
      records: []
    };
  },
  methods: {
    async fetchRecords() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/records');
        this.records = response.data;
      } catch (error) {
        console.error('Error fetching records:', error);
      }
    }
  },
  mounted() {
    this.fetchRecords();
  }
};
</script>

<style scoped>
#app {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f0f0f0;
  padding: 20px;
  box-sizing: border-box;
}

.container {
  background-color: white;
  padding: 40px;
  max-width: 800px; /* Increased width for better spacing */
  width: 100%;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  font-family: Arial, sans-serif;
  text-align: center; /* Center-aligns the text */
}

h1 {
  margin-bottom: 20px; /* Adds space between heading and form */
  color: black;
}

button {
  margin: 5px;
  padding: 8px 15px;
  border-radius: 5px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
</style>
