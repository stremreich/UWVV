#include "UWVV/Ntuplizer/interface/TriggerPathInfo.h"

#include <regex>

using namespace uwvv;


TriggerPathInfo::TriggerPathInfo(const std::string& nameExp) : 
  nameExp_(nameExp),
  name_(nameExp),
  bit_(999),
  isValid_(false)
{;}


void TriggerPathInfo::setup(const edm::TriggerNames& names)
{
  std::regex re(nameExp_);
  bit_ = names.size();
  for(size_t i = 0; i < names.size(); ++i)
    {
      if(std::regex_match(names.triggerName(i), re))
        {
          // There can be only one
          if(bit_ != names.size())
            throw cms::Exception("BadTriggerExpression")
              << "Two path matched trigger path expression \""
              << nameExp_ << "\" (\"" << names.triggerName(bit_)
              << "\" and \"" << names.triggerName(i) << "\")" 
              << std::endl;
          bit_ = i;
          name_ = names.triggerName(i);
        }
    }

  // No match!
  if(bit_ == names.size())
    throw cms::Exception("BadTriggerExpression")
      << "No path matched trigger path expression \""
      << nameExp_ << "\"."
      << std::endl;
  
  isValid_ = true;
}


bool TriggerPathInfo::pass(const edm::TriggerResults& results) const
{
  if(!isValid_)
    explode();

  return results.accept(bit_);
}


unsigned 
TriggerPathInfo::prescale(const pat::PackedTriggerPrescales& prescales) const
{
  if(!isValid_)
    explode();

  return prescales.getPrescaleForIndex(bit_);
}

