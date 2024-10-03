<template>
  <div class="record-list">
    <h2>Records</h2>
    <div v-if="loading" class="loading">loading...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <table v-else>
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
        <tr v-for="record in localRecords" :key="record.id">
        <template v-if="editingId === record.id">
          <td><input v-model="editedRecord.first_name" placeholder="First Name" class="edit-input"></td>
          <td><input v-model="editedRecord.last_name" placeholder="Last Name" class="edit-input"></td>
          <td><input v-model="editedRecord.phone" placeholder="Phone" class="edit-input"></td>
          <td><input v-model="editedRecord.city" placeholder="City" class="edit-input"></td>
          <td>
            <button @click="updateRecord(record.id)" class="save-button">Save</button>
            <button @click="cancelEdit" class="cancel-button">Cancel</button>
          </td>
        </template>
        <template v-else>
            <td>{{ record.first_name }}</td>
             <td>{{ record.last_name }}</td>
             <td>{{ record.phone }}</td>
             <td>{{ record.city }}</td>
             <td>
               <button class="edit-button" @click="editRecord(record)">Edit</button>
                <button class="delete-button" @click="confirmDelete(record.id)">Delete</button>
             </td>
        </template>
        </tr>
      </tbody>
    </table>

    <div v-if="showConfirmDialog" class="confirm-dialog">
      <p>Are you sure you want to delete this record?</p>
      <button @click="executeDelete" class="delete-button">Yes, Delete</button>
      <button @click="cancelDelete" class="cancel-delete">Cancel</button>
    </div>


  </div>
</template>

<script>
import axios from 'axios';

const API_URL = import.meta.env.VITE_BACKEND_URL

export default {
  name: 'RecordList',
  props: {
    records: Array,
    required: true
  },
  data() {
    return {
      localRecords: [...this.records],
      editingId: null,
      editedRecord: {},
      loading: false,
      error: null,
      showConfirmDialog: false,
      recordToDelete: null
    };
  },
  watch: {
    records(newRecords) {
      this.localRecords = [...newRecords];
    }
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
      this.loading = true;
      this.error = null;
      try {
        await axios.put(`${API_URL}/records/${id}`, this.editedRecord);
        this.$emit('record-updated');
        this.cancelEdit();
      } catch (error) {
        this.error = 'Error updating recorc. Please try again.'
        console.error('Error updating record:', error);
      } finally {
        this.loading = false;
      }
    },
    confirmDelete(id) {
      this.recordToDelete = id;
      this.showConfirmDialog = true;
    },
    cancelDelete() {
      this.recordToDelete = null;
      this.showConfirmDialog = false;
    },
    async executeDelete() {
      this.loading = true;
      this.error = null;
      try {
        await axios.delete(`${API_URL}/records/${this.recordToDelete}`);
        this.localRecords = this.localRecords.filter(record => record.id !== this.recordToDelete);
        this.$emit('record-deleted', this.recordToDelete);
        this.showConfirmDialog = false;
      } catch (error) {
        this.error = 'Error deleting record. Please try again.'
        console.error('Error deleting record:', error);
      } finally {
        this.loading = false;
        this.recordToDelete = null;
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
  position: relative;
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
  padding: 12px;
  border-bottom: 1px solid #eee;
  text-align: left;
  color:#333
}

thead th {
  background-color: #f9f9f9;
  font-weight: 600;
}

.edit-input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
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

.save-button {
  background-color: #2196F3;
  color: white;
  margin-right: 8px;
}

.cancel-button {
  background-color: #9e9e9e;
  color: white;
}

button:hover {
  opacity: 0.9;
}

.loading{
  text-align: center;
  padding: 20px;
}

.error {
  color: #f44336;
}

.confirm-dialog {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  color: black;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 1000;
}
</style>
