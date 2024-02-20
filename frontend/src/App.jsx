import { Input, Button, Select, Option } from "@material-tailwind/react";

function App() {
  return (
    <>
      <section className="container mx-auto">
        <div className="p-4 mt-20 flex flex-col gap-4 max-w-xl">
          <Input size="md" label="test input" />
          <Button color="blue">Blue Button</Button>
          <Select size="md" label="Select Version">
            <Option>Material Tailwind HTML</Option>
            <Option>Material Tailwind React</Option>
            <Option>Material Tailwind Vue</Option>
            <Option>Material Tailwind Angular</Option>
            <Option>Material Tailwind Svelte</Option>
          </Select>
        </div>
      </section>
    </>
  )
}

export default App
