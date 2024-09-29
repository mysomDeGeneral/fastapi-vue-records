<template>
  <div class="record-list">
    <h2>Records</h2>
    <table>
      <thead>
        <tr>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Phone</th>
          <th>City</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="record in records" :key="record.id">
        <template v-if="editingId === record.id">
          <td><input v-model="editedRecord.first_name" placeholder="First Name"></td>
          <td><input v-model="editedRecord.last_name" placeholder="Last Name"></td>
          <td><input v-model="editedRecord.phone" placeholder="Phone"></td>
          <td><input v-model="editedRecord.city" placeholder="City"></td>
          <td>
            <button @click="updateRecord(record.id)">Save</button>
            <button @click="cancelEdit">Cancel</button>
          </td>
        </template>
        <template v-else>
            <td>{{ record.first_name }}</td>
             <td>{{ record.last_name }}</td>
             <td>{{ record.phone }}</td>
             <td>{{ record.city }}</td>
             <td>
               <button class="edit-button" @click="editRecord(record)">Edit</button>
                <button class="delete-button" @click="deleteRecord(record.id)">Delete</button>
             </td>
        </template>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
import axios from 'axios';

const API_URL = import.meta.env.VITE_BACKEND_URL

export default {
  name: 'RecordList',
  props: {
    records: Array
  },
  data() {
    return {
      editingId: null,
      editedRecord: {}
    };
  },
  methods: {
    editRecord(record) {
      this.editingId = record.id;
      this.editedRecord = { ...record };
    },
    cancelEdit() {
      this.editingId = null;
      this.editedRecord = {};
    },
    async updateRecord(id) {
      try {
        await axios.put(`${API_URL}/records/${id}`, this.editedRecord);
        this.$emit('record-updated');
        this.cancelEdit();
      } catch (error) {
        console.error('Error updating record:', error);
      }
    },
    async deleteRecord(id) {
      try {
        await axios.delete(`${API_URL}/records/${id}`);
        this.$emit('record-deleted');
      } catch (error) {
        console.error('Error deleting record:', error);
      }
    }
  }
};
</script>

<style scoped>
h2 {
  color: black;
}

.record-list {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

ul {
  list-style: none;
  padding: 0;
}

li {
  margin-bottom: 15px;
  padding-bottom: 10px;
  border-bottom: 1px solid #eee;
}

.record-details {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

span {
  font-size: 1rem;
  color: #333;
}

button {
  margin-left: 10px;
  padding: 8px 12px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 10px;
  border-bottom: 1px solid #eee;
  text-align: left;
  color:#333
}

thead th {
  background-color: #f9f9f9;
}

.edit-button {
  background-color: #f0ad4e;
  color: white;
  padding: 5px 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.delete-button {
  background-color: #d9534f;
  color: white;
  padding: 5px 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  opacity: 0.9;
}
</style>
