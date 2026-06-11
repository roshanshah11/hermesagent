# Updating properties on existing blocks

## Pattern that works (verified 2026-06-10)

To modify properties on an existing block (e.g., update a task's title or due date):

1. Read the current block state:
   ```python
   block_record = notion_v3._rec("block", block_id)
   current_properties = block_record.get('properties', {})
   ```

2. Create a modified properties object:
   ```python
   # Start with current properties
   updated_properties = dict(current_properties)  # Shallow copy
   
   # Modify specific properties
   # For title/text properties:
   updated_properties[title_prop_id] = [["New Title Text"]]
   
   # For date properties:
   updated_properties[due_prop_id] = [["‣", [["d", {
       "type": "datetime",
       "time_zone": "America/New_York",
       "start_date": "2026-06-11",
       "start_time": "09:00"
   }]]]]
   
   # For select properties:
   updated_properties[status_prop_id] = [["In Progress"]]
   ```

3. Set the entire properties object:
   ```python
   notion_v3.save_transactions([
       notion_v3.op(block_id, ["properties"], "set", updated_properties)
   ])
   ```

4. Verify the update:
   ```python
   updated_record = notion_v3._rec("block", block_id)
   # Check that your changes are present
   ```

## Why this works
- The properties object is a direct child of the block's value object
- Setting the entire properties object avoids "incomplete_ancestor_path" errors
- This approach is simpler than trying to create new blocks or modify nested objects
- All property types (text, title, date, select, checkbox, etc.) use the same pattern

## Property value formats (confirmed working)
- text/title: `[[\"some text\"]]`
- date/datetime: `[[\"‣\",[[\"d\",{\"type\":\"datetime\",\"start_date\":\"YYYY-MM-DD\",\"start_time\":\"HH:MM\",\"time_zone\":\"America/New_York\"}]]]]`
  - Note: The "‣" prefix and nested array format is required
- select: `[[\"<Option Name>\"]]` (must match existing option value exactly)
- checkbox: `[["true"]]` or `[["false"]]` or `[["Yes"]]` / `[["No"]]`
- relation: `[["‣",[["p","<TARGET_ROW_ID>","<SPACE>"]]]]`

## Important notes
- Do NOT attempt to set nested objects like ["value", "value"] or ["value"] - this will result in "incomplete_ancestor_path" errors
- Do NOT attempt to set the ID field in the value object when updating existing blocks
- Always verify your changes by reading the block back after setting properties