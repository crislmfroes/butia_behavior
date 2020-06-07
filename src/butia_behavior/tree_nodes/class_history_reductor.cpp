#include "behaviortree_cpp_v3/behavior_tree.h"
#include "stdlib.h"
#include "list"
#include "map"
class ClassHistoryReductorAction : public BT::SyncActionNode
{

public:
    ClassHistoryReductorAction(const std::string &name, const BT::NodeConfiguration &config) : BT::SyncActionNode(name, config)
    {
    }

    static BT::PortsList providedPorts()
    {
        return {
            BT::InputPort<int(std::list<int>)>("reduction_function"),
            BT::InputPort<std::map<std::string, std::list<int>>>("counts_history"),
            BT::OutputPort<std::map<std::string, int>>("classes_count")};
    }

    BT::NodeStatus tick() override
    {
        auto reductionOptional = this->getInput<int(std::list<int>)>("reduction_function");
        auto countsHistoryOptional = this->getInput<std::map<std::string, std::list<int>>>("counts_history");
        if (!reductionOptional)
        {
            throw BT::RuntimeError("missing required input [reduction_functionc]: ", reductionOptional.error());
        }
        if (!countsHistoryOptional)
        {
            throw BT::RuntimeError("missing required input [counts_history]: ", countsHistoryOptional.error());
        }
        std::map<std::string, int> classesCount;
        for (auto &&pair : countsHistoryOptional.value())
        {
            classesCount[pair.first] = reductionOptional.value()(pair.second);
        }
        this->setOutput("classes_count", classesCount);
        return BT::NodeStatus::SUCCESS;
    }
};