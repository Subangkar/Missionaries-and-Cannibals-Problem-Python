class Direction:
	OLD_TO_NEW = 1
	NEW_TO_OLD = 0


class CONST:
	def __init__(self, MAX_M, MAX_C, CAP_BOAT, MAX_TIME_S, MAX_NODES):
		self.MAX_M = MAX_M
		self.MAX_C = MAX_C
		self.CAP_BOAT = CAP_BOAT

		self.MAX_TIME = MAX_TIME_S
		self.MAX_NODES = MAX_NODES

# TERMINAL_STATE = State(-1, -1, Direction.NEW_TO_OLD, -1, -1, 0)
# INITIAL_STATE = None
# #	State(MAX_M, MAX_C, Direction.OLD_TO_NEW, 0, 0,0)
