#!/usr/bin/env python3
"""
Verification script for Notion block operations
Usage: python verify_notion_block.py <block_id> <expected_properties_json>
Example: 
  python verify_notion_block.py 2518cccc-a3bf-48f6-893e-524ad7dea2e9 '{"title": "[[\\"HERMES E2E — archive me\\"]]"}"
"""

import sys
import json
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'mcp'))

import notion_v3

def verify_block(block_id, expected_props_dict):
    """
    Verify that a Notion block has the expected properties
    
    Args:
        block_id: The Notion block ID to verify
        expected_props_dict: Dictionary mapping property IDs to expected values
        
    Returns:
        bool: True if verification passes, False otherwise
    """
    try:
        # Read the block
        block_record = notion_v3._rec("block", block_id)
        actual_props = block_record.get('properties', {})
        
        # Check each expected property
        all_good = True
        for prop_id, expected_value in expected_props_dict.items():
            if prop_id not in actual_props:
                print(f"❌ FAIL: Property {prop_id} not found in block")
                all_good = False
                continue
                
            actual_value = actual_props[prop_id]
            if actual_value != expected_value:
                print(f"❌ FAIL: Property {prop_id} mismatch")
                print(f"   Expected: {expected_value}")
                print(f"   Actual:   {actual_value}")
                all_good = False
            else:
                print(f"✅ PASS: Property {prop_id} matches")
                
        # Report on any unexpected properties (just info)
        unexpected = set(actual_props.keys()) - set(expected_props_dict.keys())
        if unexpected:
            print(f"ℹ️  INFO: Block has additional properties: {list(unexpected)}")
            
        return all_good
        
    except Exception as e:
        print(f"❌ ERROR: Failed to verify block: {e}")
        return False

def verify_archived(block_id):
    """
    Verify that a Notion block is archived (alive=false)
    
    Args:
        block_id: The Notion block ID to check
        
    Returns:
        bool: True if block is archived, False otherwise
    """
    try:
        block_record = notion_v3._rec("block", block_id)
        is_alive = block_record.get('alive', True)
        if not is_alive:
            print(f"✅ PASS: Block {block_id} is archived (alive=false)")
            return True
        else:
            print(f"❌ FAIL: Block {block_id} is not archived (alive=true)")
            return False
    except Exception as e:
        print(f"❌ ERROR: Failed to check archive status: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
        
    block_id = sys.argv[1]
    try:
        expected_props = json.loads(sys.argv[2])
    except json.JSONDecodeError as e:
        print(f"❌ ERROR: Invalid JSON for expected properties: {e}")
        sys.exit(1)
        
    print(f"Verifying block {block_id}...")
    print(f"Expected properties: {expected_props}")
    print()
    
    props_ok = verify_block(block_id, expected_props)
    print()
    
    # Also check if it's archived if we have an alive property expectation
    if 'alive' in [k for k in expected_props.keys() if k.endswith('alive')] or len(sys.argv) > 3 and sys.argv[3] == '--check-archived':
        archived_ok = verify_archived(block_id)
        print()
        if props_ok and archived_ok:
            print("🎉 ALL CHECKS PASSED")
            sys.exit(0)
        else:
            print("💥 SOME CHECKS FAILED")
            sys.exit(1)
    elif props_ok:
        print("🎉 PROPERTY CHECK PASSED")
        sys.exit(0)
    else:
        print("💥 PROPERTY CHECK FAILED")
        sys.exit(1)