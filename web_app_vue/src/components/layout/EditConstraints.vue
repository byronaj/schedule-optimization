<template>
  <modal @close="toggleShowModal">
    <header class="modal-card-head">
        <p class="modal-card-title">
        Edit Constraints
        </p>
        <button class="delete" aria-label="close" @click="toggleShowModal"></button>
    </header>

    <section class="modal-card-body" style="color:black;">
        <div class="field">
        <label class="checkbox">
            <input type="checkbox">
            Shifts no more than 8 hours
        </label>
        </div>

        <div class="field">
        <label class="checkbox">
            <input type="checkbox">
            Allow back-to-back shifts
        </label>
        </div>
    </section>

    <footer class="modal-card-foot">
        <button class="button is-success">
        Save changes
        </button>
        <button class="button" aria-label="close" @click="toggleShowModal">
        Cancel
        </button>
    </footer>

    </modal>
</template>

<script>
import Modal from "@/components/Modal.vue";

export default {
  components: {Modal},
  name: 'EditConstraints',
  data() {
    return {
      showModal: false,
    }
  },
  methods: {
      toggleShowModal() {
          this.$parent.toggleEditConstraints()
      }
  }
}
</script>

<style>

</style>