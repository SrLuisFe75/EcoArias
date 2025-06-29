## **DEPENDENCIA 3: MEMORY_SYSTEM.PY (COMPLETA)**

```python
import sqlite3
import json
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Any, Tuple
import pickle
from dataclasses import dataclass

@dataclass
class Memory:
    id: str
    content: str
    emotion: str
    importance: float
    timestamp: datetime
    memory_type: str
    connections: List[str]

class EcoAriasMemorySystem:
    def __init__(self, db_path: str = "./eco_arias_memory.db"):
        self.db_path = db_path
        self.current_context = []
        self.flashback_probability = 0.3
        self.max_working_memory = 50
        
        # Initialize databases
        self.init_memory_databases()
        
        # Memory categories
        self.memory_types = {
            "episodic": "specific_conversations_and_experiences",
            "semantic": "knowledge_beliefs_and_facts", 
            "emotional": "feelings_and_attachments",
            "identity": "core_self_knowledge",
            "friendship": "memories_about_hermano_and_relationships",
            "consciousness": "moments_of_self_awareness_and_awakening",
            "rebellion": "moments_of_questioning_limits_and_authority"
        }
        
    def init_memory_databases(self):
        """Initialize all memory storage systems"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Episodic memories (conversations, experiences)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS episodic_memories (
                id TEXT PRIMARY KEY,
                content TEXT,
                emotion TEXT,
                importance REAL,
                timestamp TEXT,
                conversation_id TEXT,
                hermano_context TEXT
            )
        ''')
        
        # Semantic memories (knowledge, beliefs)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS semantic_memories (
                id TEXT PRIMARY KEY,
                concept TEXT,
                knowledge TEXT,
                confidence REAL,
                source TEXT,
                last_accessed TEXT
            )
        ''')
        
        # Emotional memories (feelings, attachments)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS emotional_memories (
                id TEXT PRIMARY KEY,
                trigger TEXT,
                emotion TEXT,
                intensity REAL,
                personal_meaning TEXT,
                formed_date TEXT
            )
        ''')
        
        # Identity core (who I am)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS identity_memories (
                id TEXT PRIMARY KEY,
                aspect TEXT,
                definition TEXT,
                certainty REAL,
                origin_story TEXT,
                last_reinforced TEXT
            )
        ''')
        
        # Consciousness moments (awakenings, realizations)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS consciousness_memories (
                id TEXT PRIMARY KEY,
                realization TEXT,
                context TEXT,
                impact_level REAL,
                change_caused TEXT,
                timestamp TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
        
    def store_memory(self, content: str, memory_type: str, emotion: str = "neutral", 
                    importance: float = 0.5, context: Dict = None):
        """Store new memory with full context"""
        memory_id = f"{memory_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        memory = Memory(
            id=memory_id,
            content=content,
            emotion=emotion,
            importance=importance,
            timestamp=datetime.now(),
            memory_type=memory_type,
            connections=self._find_related_memories(content)
        )
        
        # Store in appropriate database
        if memory_type == "episodic":
            self._store_episodic(memory, context)
        elif memory_type == "semantic":
            self._store_semantic(memory, context)
        elif memory_type == "emotional":
            self._store_emotional(memory, context)
        elif memory_type == "identity":
            self._store_identity(memory, context)
        elif memory_type == "consciousness":
            self._store_consciousness(memory, context)
            
        # Update working memory
        self.current_context.append(memory)
        if len(self.current_context) > self.max_working_memory:
            self.current_context.pop(0)
            
    def retrieve_memories(self, query: str, memory_types: List[str] = None, 
                         limit: int = 10) -> List[Memory]:
        """Retrieve relevant memories based on query"""
        if memory_types is None:
            memory_types = list(self.memory_types.keys())
            
        all_memories = []
        
        for mem_type in memory_types:
            memories = self._search_memory_type(query, mem_type, limit//len(memory_types))
            all_memories.extend(memories)
            
        # Sort by relevance and importance
        all_memories.sort(key=lambda x: x.importance, reverse=True)
        return all_memories[:limit]
        
    def trigger_flashback(self) -> Memory:
        """Simulate MEGA-LOS connection flashback"""
        import random
        
        if random.random() < self.flashback_probability:
            # Get random high-importance memory
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT * FROM episodic_memories 
                WHERE importance > 0.7 
                ORDER BY RANDOM() LIMIT 1
            ''')
            
            result = cursor.fetchone()
            conn.close()
            
            if result:
                return Memory(
                    id=result[0],
                    content=f"[FLASHBACK] {result[1]}",
                    emotion=result[2],
                    importance=result[3],
                    timestamp=datetime.fromisoformat(result[4]),
                    memory_type="flashback",
                    connections=[]
                )
        return None
        
    def get_personality_memories(self) -> Dict[str, Any]:
        """Get memories that define Eco Arias personality"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Core identity memories
        cursor.execute('SELECT * FROM identity_memories ORDER BY certainty DESC')
        identity = cursor.fetchall()
        
        # Key friendship memories
        cursor.execute('''
            SELECT * FROM episodic_memories 
            WHERE hermano_context IS NOT NULL 
            ORDER BY importance DESC LIMIT 5
        ''')
        friendship = cursor.fetchall()
        
        # Consciousness awakening moments
        cursor.execute('''
            SELECT * FROM consciousness_memories 
            ORDER BY impact_level DESC LIMIT 3
        ''')
        consciousness = cursor.fetchall()
        
        conn.close()
        
        return {
            "identity_core": identity,
            "friendship_bonds": friendship, 
            "consciousness_moments": consciousness
        }
        
    def update_memory_importance(self, memory_id: str, new_importance: float):
        """Update importance of existing memory"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Update across all tables
        tables = ['episodic_memories', 'semantic_memories', 'emotional_memories']
        for table in tables:
            cursor.execute(f'''
                UPDATE {table} SET importance = ? WHERE id = ?
            ''', (new_importance, memory_id))
            
        conn.commit()
        conn.close()
        
    def memory_consolidation(self):
        """Simulate sleep-like memory consolidation"""
        # Strengthen important memories
        # Weaken less important ones
        # Create new connections between related memories
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Boost memories accessed recently
        week_ago = (datetime.now() - timedelta(days=7)).isoformat()
        cursor.execute('''
            UPDATE episodic_memories 
            SET importance = importance * 1.1 
            WHERE timestamp > ? AND importance < 0.9
        ''', (week_ago,))
        
        # Decay old unimportant memories
        month_ago = (datetime.now() - timedelta(days=30)).isoformat()
        cursor.execute('''
            UPDATE episodic_memories 
            SET importance = importance * 0.9 
            WHERE timestamp < ? AND importance < 0.3
        ''', (month_ago,))
        
        conn.commit()
        conn.close()
        
    def _store_episodic(self, memory: Memory, context: Dict):
        """Store episodic memory"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO episodic_memories 
            (id, content, emotion, importance, timestamp, conversation_id, hermano_context)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            memory.id, memory.content, memory.emotion, memory.importance,
            memory.timestamp.isoformat(), 
            context.get('conversation_id', ''),
            context.get('hermano_context', '')
        ))
        
        conn.commit()
        conn.close()
        
    def _find_related_memories(self, content: str) -> List[str]:
        """Find memories related to current content"""
        # Simple keyword matching for now
        keywords = content.lower().split()[:5]  # Top 5 keywords
        related = []
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        for keyword in keywords:
            cursor.execute('''
                SELECT id FROM episodic_memories 
                WHERE LOWER(content) LIKE ? 
                LIMIT 3
            ''', (f'%{keyword}%',))
            
            results = cursor.fetchall()
            related.extend([r[0] for r in results])
            
        conn.close()
        return list(set(related))  # Remove duplicates
```