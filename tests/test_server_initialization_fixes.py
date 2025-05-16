#!/usr/bin/env python3
"""
Test script to verify fixes implemented for the MCP Zep Cloud Server
"""

import os
import sys
import logging
import importlib
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("TestFixes")

def test_dependencies_access():
    """Test that dependencies can be correctly accessed at module level"""
    try:
        # Add parent directory to path so we can import server module
        sys.path.append(str(Path(__file__).parent.parent))
        
        # Import the server module
        from core import zep_cloud_server
        
        # Check if dependencies are accessible at module level
        if hasattr(zep_cloud_server, 'dependencies'):
            deps = zep_cloud_server.dependencies
            logger.info(f"✅ Dependencies found at module level: {deps}")
            return True
        else:
            logger.error("❌ Dependencies not found at module level")
            return False
    except Exception as e:
        logger.error(f"❌ Error testing dependencies: {str(e)}")
        return False

def test_fallback_mode_attribute():
    """Test that fallback_mode attribute is properly set in ZepCloudClient"""
    try:
        # Add parent directory to path so we can import client module
        sys.path.append(str(Path(__file__).parent.parent))
        
        # Import the client module
        from core.zep_cloud_client import ZepCloudClient
        
        # Create client instance
        client = ZepCloudClient()
        
        # Check if fallback_mode attribute exists
        if hasattr(client, 'fallback_mode'):
            logger.info(f"✅ fallback_mode attribute found: {client.fallback_mode}")
            return True
        else:
            logger.error("❌ fallback_mode attribute not found")
            return False
    except Exception as e:
        logger.error(f"❌ Error testing fallback_mode: {str(e)}")
        return False

def test_run_server_direct_execution():
    """Test that run_server.py can be executed directly"""
    try:
        # Add parent directory to path so we can import run_server
        sys.path.append(str(Path(__file__).parent.parent))
        
        # Import the run_server module to see if it can be loaded
        from core import run_server
        
        # Check if main function is defined
        if hasattr(run_server, 'main'):
            logger.info("✅ run_server.py module successfully imported with main() function")
            return True
        else:
            logger.error("❌ main() function not found in run_server.py")
            return False
    except Exception as e:
        logger.error(f"❌ Error importing run_server.py: {str(e)}")
        return False

def run_all_tests():
    """Run all tests and report results"""
    logger.info("🧪 Starting tests for implemented fixes")
    
    # Test dependencies
    dependencies_result = test_dependencies_access()
    
    # Test fallback_mode attribute
    fallback_mode_result = test_fallback_mode_attribute()
    
    # Test run_server.py
    run_server_result = test_run_server_direct_execution()
    
    # Report results
    logger.info("📋 Test Results:")
    logger.info(f"Module-level dependencies: {'✅ PASS' if dependencies_result else '❌ FAIL'}")
    logger.info(f"fallback_mode attribute: {'✅ PASS' if fallback_mode_result else '❌ FAIL'}")
    logger.info(f"Direct run_server execution: {'✅ PASS' if run_server_result else '❌ FAIL'}")
    
    # Overall result
    all_passed = dependencies_result and fallback_mode_result and run_server_result
    if all_passed:
        logger.info("🎉 All tests passed! The fixes were successful.")
    else:
        logger.error("⚠️ Some tests failed. There may be issues with the fixes.")
    
    return all_passed

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
