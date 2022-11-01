<template>
	<div class="select">
		<select v-model="modelValue" @change="changeOption">
			<option value="" disabled hidden>Сортировать...</option>
			<option
				v-for="option in options"
				:key="option.value"
				:value="option.value"
			>
				{{ option.name }}
			</option>
		</select>
	</div>	
</template>



<script>
export default {
	name: 'my-select',
	props: {
		modelValue: {
			type: String
		},
		options: {
			type: Array,
			default: () => []
		}
	},
	methods: {
		changeOption(event) {
			this.$emit('update:modelValue', event.target.value)
		}
	}
}
</script>



<style scoped>
.select {
	margin-bottom: 15px;
	display: flex;
	justify-content: center;
}
</style>